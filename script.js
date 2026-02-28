const tg = window.Telegram.WebApp;
tg.expand();

const qCount = 22;
const box = document.getElementById("questions");

for (let i = 1; i <= qCount; i++) {
  box.innerHTML += `
    <p>${i}-savol</p>
    <input id="q${i}" /><br><br>
  `;
}

function submit() {
  let data = {};
  for (let i = 1; i <= qCount; i++) {
    data[i] = document.getElementById("q" + i).value;
  }
  tg.sendData(JSON.stringify(data));
}