import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,readdirSync} from 'node:fs';
import {normalizeView,initReadingView} from '../src/lib/reading-view.js';
const read=p=>readFileSync(new URL('../'+p,import.meta.url),'utf8');
test('lockfile root metadata agrees without dependency drift',()=>{
 const pkg=JSON.parse(read('package.json')),lock=JSON.parse(read('package-lock.json'));
 assert.equal(lock.version,pkg.version);assert.equal(lock.packages[''].version,pkg.version);
 assert.deepEqual(lock.packages[''].dependencies,pkg.dependencies);
 assert.deepEqual(lock.packages[''].engines,pkg.engines);
});
test('reading preference normalizes invalid values',()=>{assert.equal(normalizeView('perspectives'),'perspectives'); for(const v of [null,undefined,'bad','synthesis'])assert.equal(normalizeView(v),'synthesis');});
test('storage denied does not disable buttons; initialization is idempotent',()=>{
 const buttons=['synthesis','perspectives'].map(view=>({dataset:{view},classList:{toggle(){}},setAttribute(k,v){this[k]=v},addEventListener(k,fn){this.click=fn;this.listeners=(this.listeners||0)+1}}));
 const control={dataset:{},hidden:true,querySelectorAll:()=>buttons};const doc={body:{dataset:{}},querySelector:()=>control};const win={get localStorage(){throw Error('denied')}};
 initReadingView(doc,win);assert.equal(doc.body.dataset.wintermuteView,'synthesis');assert.equal(control.hidden,false);buttons[1].click();assert.equal(doc.body.dataset.wintermuteView,'perspectives');assert.equal(buttons[1]['aria-pressed'],'true');initReadingView(doc,win);assert.equal(buttons[0].listeners,1);
});
test('site deployment and shared title contract',()=>{assert.match(read('astro.config.mjs'),/base: '\/wintermute'/);assert.match(read('.github/workflows/deploy.yml'),/node-version: 24/);assert.match(read('src/layouts/BlogPost.astro'),/<h1>\{title\}<\/h1>/);assert.doesNotMatch(read('src/pages/archive.astro'),/data-filter=/);});
test('all source articles defer H1 to layout; views are explicit',()=>{const files=readdirSync(new URL('../src/content/posts/',import.meta.url));assert.equal(files.length,13);let views=0;for(const f of files){const text=read('src/content/posts/'+f);assert.doesNotMatch(text,/^# /m);if(text.includes('readingViews: true'))views++;}assert.equal(views,7);});
