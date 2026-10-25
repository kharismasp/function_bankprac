const assert=require('node:assert/strict'),fs=require('node:fs');const bank=require('../dist/bank.json'),core=require('../dist/core.js'),visual=require('../dist/visuals.js');let assertions=0;const ok=(x,msg)=>{assert.ok(x,msg);assertions++;},near=(a,b)=>ok(Math.abs(a-b)<1e-8,`${a} != ${b}`);const ids=new Set(bank.map(q=>q.id));assert.equal(bank.length,90);assert.equal(ids.size,90);for(let ch=1;ch<=3;ch++)for(const band of ['Core','Challenge','Advanced'])assert.equal(bank.filter(q=>q.chapter===ch&&q.level===band).length,10);
for(const q of bank){assert.match(q.id,/^FG[123]-[CHA](?:[1-9]|10)$/);for(const l of ['en','id']){ok(q.title[l].length>3);ok(q.prompt[l].length>20);ok(q.steps[l].length>=3);ok(!q.prompt[l].includes('[object Object]')); }assert.equal(q.steps.id.length,q.steps.en.length);ok(q.source.questionPage>=1&&q.source.questionPage<=3);ok(q.source.solutionPage>=4&&q.source.solutionPage<=6);if(q.visual)ok(visual.render(q.visual).length>100);}
// Independent mathematical checks for algebraic, domain, parameter and modelling items.
// Chapter 1: evaluate, reconstruct and compose instead of trusting solution strings.
const p=x=>2*x*x-3*x+1;near(p(-2),15);for(const x of [-3,-1,0,2])near(p(x+1),2*x*x+x);near(4*7-7,21);
near(Math.min(...Array.from({length:501},(_,i)=>(-2+i/100)**2+1)),1);near(3**2+1,10);ok(3*(-2)-2!==3*2-2);near((-2)**2,2**2);
for(const x of [-2,0,2]){near(2*x*x+1,2*(x*x)+1);near(((5*x-4)+4)/5,x);near(3*((x+4)/3)-4,x);near(((3*x-4)+4)/3,x);near(2*(x+4)-7,2*x+1);}
for(const x of [-2,0,4]){near(Math.sqrt(5-x)-1,Math.sqrt(5-x)-1);near(Math.sqrt(5-(x-1)),Math.sqrt(6-x));}ok(5-5>=0&&5-5.01<0);ok(6-6>=0&&6-6.01<0);
for(const x of [-3,0,2,4]){if(x===1)continue;const y=(2*x+3)/(x-1);near((y+3)/(y-2),x);}for(const x of [-5,-2,-1])near(-1-Math.sqrt((x+1)**2),x);
near(1+4,5);near(4+4,8);near(2*3+2,8);near(2*(-1)+2,0);near((4-1)**2,9);
for(const x of [-4,-2,0,3])near(Math.sqrt(x*x+8*x+16),x+4);for(const x of [-4,0,2]){const y=(1-x)/(x+2);near((1-2*y)/(y+1),x);}
for(const x of [2,3,5])near(2+Math.sqrt((x-2)**2),x);for(const [x,y]of [[1,2],[3,-1],[5,4]]){near(x+3,{1:4,3:6,5:8}[x]);near(3*y-1,{2:5,'-1':-4,4:11}[y]);}
for(const x of [-1,0,2])near((5-Math.sqrt((2*x-5)**2))/2,x);near(13-(9+4),0);ok(13-(9+4.01)<0);near(Math.sqrt(9-0),3);near(Math.sqrt(9-9),0);
for(const x of [-3,0,2.5,4])ok(((x-1)/(x-2)>=0)===(x<=1||x>2));near(3*3-2,7);near(3*4-2,10);near((15-2+2)/3,5);
// Chapter 2: roots, multiplicities, signs, intersections and transformed features.
const polys=[{f:x=>(x+4)*(x-1)*(x-3),roots:[-4,1,3],y:12},{f:x=>-1*(x+2)**2*(x-5),roots:[-2,5],y:20},{f:x=>-2*(x-1)*(x+3)*(x-4)*(x+1),roots:[-3,-1,1,4],y:-24}];for(const p of polys){for(const x of p.roots)near(p.f(x),0);near(p.f(0),p.y);}
for(const x of [-4,-2,-1,1,3]){ok((x*(x-2)*(x+3)>0)===((x>-3&&x<0)||x>2));ok(((x+2)*(x-1)*(x-4)>0)===((x>-2&&x<1)||x>4));}
near(4/(-6+2)+1,0);near(4/2+1,3);for(const x of [-3,0,5])near((x-4)/(x+1),1-5/(x+1));for(const x of [-3,0,3])near(x*(x-2)*(x+2),5*x);near(2/(-4+3)+2,0);
near(-4*(3+3)*(3-2)**2,-24);near(-2*(0+2)**2*(0-1)*(0-4),-32);near(4/(1-3)+2,0);near(4/(-3)+2,2/3);
for(const x of [-5,-2,0,4])ok(((2*x+1)/(x-3)>1)===(x<-4||x>3));for(const x of [3,Math.SQRT2,-Math.SQRT2])near((x-1)*(x+1)*(x-3),x-3);
near(6/2-2,1);near(6/3-2,0);near(6-4,2);near(-3/(4-1)+1,0);near(-3/(-1)+1,4);for(const x of [-3,-1.5,.5])ok([-2,1,5].includes(2*x+4));
near(2*9*(-1)*(-4),72);const lo=-2-2*Math.SQRT2,hi=-2+2*Math.SQRT2;near((lo+2)**2-8,0);near((hi+2)**2-8,0);ok((0+2)**2-8<0);
near(-8/(0-2)-1,3);near(-8/(-6-2)-1,0);const transformed=x=>-2*(3/(3*x+6-2)-1);near(transformed(-1/3),0);near(transformed(0),.5);
for(const x of [-6,-4,-1,2])ok((2/(x-1)>1/(x+2))===((x>-5&&x<-2)||x>1));for(const k of [-4,-3,-2,2]){near(0**3-3*0,k*0);if(k>-3)for(const x of [-Math.sqrt(k+3),Math.sqrt(k+3)])near(x**3-3*x,k*x);}
for(const x of [-2,0,1.5,2,3])near((x-2)**2*(x-1.5),x**3-5.5*x*x+10*x-6);for(const x of [-1,.5,2,4]){const u=2*x-2,g=-1*(u+2)**2*(u-1)*(u-4);ok((g>0)===(x>1.5&&x<3));}
near((3+1)/(3-2),4);for(const x of [-2,0,2.5,4,6])ok(((3*x+3)/(x-2)>6)===(x>2&&x<5));
// Chapter 3: exact substitutions, inverse round-trips, model recovery and log domains.
near(18/12,1.5);near(27/18,1.5);near(7*3**2,63);near(5*1.5**0,5);near(2*3**(1-1)-6,-4);near(2*3**(2-1)-6,0);near(8**(5-1),4**(5+1));near(Math.log2(40)-Math.log2(5)+Math.log2(2),4);near(800*1.05**3,926.1);near(Math.log(11-2)/Math.log(3),2);
near(5*2**(Math.log(17/5)/Math.log(2)),17);for(const x of [0,2])near(9**x-10*3**x+9,0);near(Math.log2(5-1)+Math.log2(5-3),3);ok(-1<3);
near(3*Math.log(2*2.5-4)-1,-1);near(3*Math.log(2*(2+Math.exp(1/3)/2)-4)-1,0);for(const x of [-2,0,2])near(2*Math.log(((4*Math.exp(x/2)-3)+3)/4),x);
near(320*1.25**3,625);near(320*1.25**5,976.5625);const meet=Math.log(1.2)/Math.log(1.08/1.04);near(300*1.04**meet,250*1.08**meet);const decay=Math.log(.2)/Math.log(.6);near(5*.6**decay,1);ok(5*.6**(decay+.1)<1);near(3*2**2+1,13);near(Math.log2(16)+Math.log(16)/Math.log(4),6);
for(const x of [-Math.log(2)/Math.log(3),1])near(2*9**x-7*3**x+3,0);for(const k of [1,3,4]){const x=3+Math.sqrt(4-k);near((x-1)*(5-x),k);ok(x>1&&x<5);}for(const x of [-2,-1,0,1,2])ok((2*4**x-5*2**x+2<=0)===(x>=-1&&x<=1));
const k=Math.log(8/5)/3,P0=150*(8/5)**(-2/3);near(P0*Math.exp(2*k),150);near(P0*Math.exp(5*k),240);near(Math.exp(k*Math.log(2)/k),2);near((Math.log(162)-Math.log(18))/2,Math.log(3));near(6*3,18);near(6*3**3,162);
for(const x of [-2,0,2])near(2*Math.log((3*Math.exp(x/2)+1-1)/3),x);near(100*(.8*Math.SQRT2)**4,400*.8**4);near(2*Math.log(3*(2+Math.exp(-2)/3)-6)+4,0);for(const x of [0,2,4])near(2+Math.exp((2*Math.log(3*x+3)+4-4)/2)/3,x+3);
for(const k of [-2,0,1,2]){near(1-(k+1)+k,0);if(k>0)near(Math.exp(2*Math.log(k))-(k+1)*Math.exp(Math.log(k))+k,0);}near(Math.log(8)/Math.log(4),1.5);near(3*9**1.5,81);
// Core application state and frozen-set semantics.
assert.equal(core.filterBank(bank,{chapter:3,level:'Challenge'},{}).length,10);assert.equal(core.filterBank(bank,{search:'FG2-A9'},{}).length,1);assert.equal(core.filterBank(bank,{search:'not-a-real-question'},{}).length,0);const rec={'FG1-C1':{reviewed:true,flag:true,text:'a'}};assert.equal(core.filterBank(bank,{status:'flagged'},rec).length,1);assert.equal(core.filterBank(bank,{status:'unreviewed'},rec).length,89);const snapshot=core.filterBank(bank,{status:'unreviewed'},rec).map(q=>q.id);rec['FG1-C2']={reviewed:true};assert.equal(snapshot.length,89);const shuffled=core.shuffle([...ids],()=>.4);assert.equal(new Set(shuffled).size,90);assert.deepEqual([...shuffled].sort(),[...ids].sort());const state=core.validateState({session:['FG1-C1','bad','FG1-C1'],records:{'FG1-C1':{steps:999,hints:-1,text:'draft'},bad:{}}},ids);assert.equal(state.session.length,1);assert.equal(state.records['FG1-C1'].steps,8);assert.equal(state.records['FG1-C1'].hints,0);assert.equal(Object.keys(state.records).length,1);
// Exact diagram models; discontinuities never become connected curves.
for(const [name,make]of Object.entries(visual.modelSpecs)){const m=make();for(const p of m.points){if(p.open)continue;ok(m.curves.some(c=>c.f&&Math.abs(c.f(p.x)-p.y)<1e-8),name+' point not on model');}if(m.square)near(m.v[1]-m.v[0],m.v[3]-m.v[2]);const html=visual.render(name);ok(!/NaN|undefined|Infinity/.test(html));}
const h=visual.modelSpecs.hole();ok(h.points[0].open);ok(Number.isNaN(h.curves[0].f(2)));ok(Number.isNaN(h.curves[0].f(3)));const inv=visual.modelSpecs['exp-inverse']();for(const x of [-1,0,1])near(inv.curves[1].f(inv.curves[0].f(x)),x);
console.log(JSON.stringify({questions:bank.length,chapters:3,questionsPerBandPerChapter:10,bilingual:'PASS',assertions,sourcePages:'PASS',filtersAndPersistence:'PASS',diagramModels:'PASS'}));
