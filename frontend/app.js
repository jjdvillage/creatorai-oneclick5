const ENV_API = window.__API_URL__ || null;
const API = ENV_API || localStorage.getItem('API_URL') || 'http://localhost:8000';
const emailEl=document.getElementById('email'),pwEl=document.getElementById('password'),out=document.getElementById('output');
const reg=document.getElementById('registerBtn'),log=document.getElementById('loginBtn'),logout=document.getElementById('logoutBtn'),stat=document.getElementById('authStatus');
function token(){return localStorage.getItem('JWT');}
function authHeaders(){return token()?{'Authorization':'Bearer '+token()}:{};}
function setLoggedIn(on){logout.style.display=on?'inline-block':'none';log.style.display=on?'none':'inline-block';reg.style.display=on?'none':'inline-block';stat.textContent=on?'Logged in':'Logged out';}
reg.onclick=async()=>{const e=emailEl.value.trim(), p=pwEl.value;if(!e||!p) return alert('Enter email and password');const r=await fetch(`${API}/auth/register`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:e,password:p})});const d=await r.json();if(d.ok){localStorage.setItem('JWT',d.token);setLoggedIn(true);} else alert(d.detail||'Registration failed');};
log.onclick=async()=>{const e=emailEl.value.trim(), p=pwEl.value;const r=await fetch(`${API}/auth/login`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:e,password:p})});const d=await r.json();if(d.ok){localStorage.setItem('JWT',d.token);setLoggedIn(true);} else alert(d.detail||'Login failed');};
logout.onclick=()=>{localStorage.removeItem('JWT');setLoggedIn(false);};
document.addEventListener('DOMContentLoaded',()=>setLoggedIn(!!token()));
document.getElementById('generateBtn').onclick=async()=>{const t=document.getElementById('topic').value.trim();if(!t) return alert('Enter a topic');out.textContent='Generating...';try{const r=await fetch(`${API}/api/generate`,{method:'POST',headers:Object.assign({'Content-Type':'application/json'},authHeaders()),body:JSON.stringify({topic:t,channel:'tiktok',tone:'fun',length_sec:30})});const d=await r.json();out.textContent=JSON.stringify(d,null,2);}catch(err){out.textContent='Error: '+err;}};