let questions = [
  {
    q: "Full form of HTML?",
    opts: ["Hyper Text Markup Language", "High Text Markup Language", "Hello Text", "None of these"],
    ans: 0
  }
];
let current = 0;
let score = 0;

function login() {
  let name = document.getElementById('studentName').value;
  if(!name){ alert("Manshi Rajak")
   return;
    }
  document.getElementById('loginBox').classList.add('hidden');
  document.getElementById('quizBox').classList.remove('hidden');
  document.getElementById('welcome').innerText = "Welcome, " + name;
  showQuestion();
}

function showQuestion(){
  let q = questions[current];
  document.getElementById('questions').innerText = "Q1. " + q.q;
  let div = document.getElementById('options');
  div.innerHTML = '';
  q.opts.forEach((o,i)=>{
    let b = document.createElement('button');
    b.innerText = o;
    b.onclick = () => {
      if(i == q.ans) score++;
      showResult();
    };
    div.appendChild(b);
  });
}

function nextQuestion() { 
showResult();
 }

function showResult() {
  document.getElementById('quizBox').classList.add('hidden');
  document.getElementById('resultBox').classList.remove('hidden');
  document.getElementById('score').innerText = "Score: " + score + "/1";
}

function showAdmin() {
  document.getElementById('loginBox').classList.add('hidden');
  document.getElementById('adminBox').classList.remove('hidden');
}

function addQuestion() {
  alert("Adding question is disable in single question mode");
}
