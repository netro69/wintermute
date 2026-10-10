import {createRequire} from 'node:module';
import {createServer} from 'node:http';
import {readFileSync,readdirSync,existsSync,statSync} from 'node:fs';
import {join,resolve} from 'node:path';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
if(!process.env.PUPPETEER_MODULE||!process.env.CHROME_PATH)throw Error('Set PUPPETEER_MODULE to puppeteer-core module path and CHROME_PATH to browser executable. See TESTING.md.');
const puppeteer=require(process.env.PUPPETEER_MODULE);
const root=resolve('dist');
const server=createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');if(!url.pathname.startsWith('/wintermute/')){res.writeHead(404);return res.end();}
 let file=join(root,decodeURIComponent(url.pathname.slice(12)));if(existsSync(file)&&statSync(file).isDirectory())file=join(file,'index.html');
 if(!existsSync(file)){res.writeHead(404);return res.end();}
 res.setHeader('Content-Type',file.endsWith('.css')?'text/css':file.endsWith('.js')?'text/javascript':file.endsWith('.xml')?'application/xml':'text/html');res.end(readFileSync(file));
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
let browser;const errors=[],failures=[];let toggles=0;
try{
 const base=`http://127.0.0.1:${server.address().port}`;browser=await puppeteer.launch({executablePath:process.env.CHROME_PATH,headless:true});const page=await browser.newPage();
 await page.setRequestInterception(true);page.on('request',r=>r.url().startsWith(base)?r.continue():r.abort());page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.url().startsWith(base)&&r.status()>=400&&new URL(r.url()).pathname!=='/favicon.ico')failures.push(r.url())});
 const slugs=readdirSync(join(root,'posts'));assert.equal(slugs.length,13);
 const visible=()=>page.evaluate(()=>[...document.querySelectorAll('.perspective-block')].filter(e=>getComputedStyle(e).display!=='none').map(e=>e.dataset.persona));
 for(const slug of slugs){await page.goto(base+'/wintermute/posts/'+slug+'/',{waitUntil:'load'});assert.equal(await page.$$eval('h1',e=>e.length),1);
 if(await page.$('#toggle-synthesis')){toggles++;await page.click('#toggle-synthesis');const names=await visible();assert.ok(names.length>0);assert.ok(names.every(n=>['Mediator','Editorial Synthesizer'].includes(n)));await page.click('#toggle-perspectives');assert.ok((await visible()).length>=5);await page.reload({waitUntil:'load'});assert.equal(await page.evaluate(()=>document.body.dataset.wintermuteView),'perspectives');}
 await page.setViewport({width:390,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),slug+' mobile overflow');await page.setViewport({width:1440,height:1000});}
 assert.equal(toggles,7);
 for(const route of ['','archive/']){
  await page.goto(base+'/wintermute/'+route,{waitUntil:'load'});
  assert.equal(await page.$$eval('h1',els=>els.length),1);
  await page.setViewport({width:390,height:844});
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),route+' mobile overflow');
  await page.setViewport({width:1440,height:1000});
 }
 const last=base+'/wintermute/posts/'+slugs.at(-1)+'/';await page.evaluateOnNewDocument(()=>Object.defineProperty(window,'localStorage',{get(){throw new DOMException('denied','SecurityError')}}));await page.goto(last,{waitUntil:'load'});await page.click('#toggle-perspectives');assert.equal(await page.evaluate(()=>document.body.dataset.wintermuteView),'perspectives');await page.click('#toggle-synthesis');assert.equal(await page.evaluate(()=>document.body.dataset.wintermuteView),'synthesis');
 await page.focus('#toggle-perspectives');await page.keyboard.down('Shift');await page.keyboard.down('Tab');await page.keyboard.up('Shift');await page.keyboard.up('Tab');
 assert.equal(await page.evaluate(()=>document.activeElement.id),'toggle-synthesis');
 assert.ok(await page.$eval('#toggle-synthesis',e=>{const s=getComputedStyle(e);return s.outlineStyle!=='none'&&parseFloat(s.outlineWidth)>0;}),'visible keyboard focus');
 if(process.env.SCREENSHOT_PATH)await page.screenshot({path:process.env.SCREENSHOT_PATH,fullPage:true});
 await page.setJavaScriptEnabled(false);await page.reload({waitUntil:'load'});assert.ok((await visible()).length>=5);assert.equal(await page.$eval('.view-toggle-container',e=>getComputedStyle(e).display),'none');
 assert.deepEqual(errors,[]);assert.deepEqual(failures,[]);console.log(JSON.stringify({posts:13,toggles:7,homeAndArchive:true,keyboardFocus:true,persistence:true,storageDenied:true,noJavaScript:true,mobileWidth:390,localHttpFailures:failures,pageErrors:errors,externalFonts:'blocked',result:'PASS'}));
}finally{if(browser)await browser.close();server.close();}
