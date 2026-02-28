const tg = window.Telegram.WebApp;
tg.expand();

const qCount = 22;
const box = document.getElementById("questions");

for (let i = 1; i <= qCount; i++) {
  const div = document.createElement("div");
  div.innerHTML = `
    <p>${i}-savol</p>
    <input id="q${i}" placeholder="Javobni kiriting">
    <hr>
  `;
  box.appendChild(div);
}

function submit() {
  let data = {};
  for (let i = 1; i <= qCount; i++) {
    data[i] = document.getElementById("q" + i).value;
  }
  tg.sendData(JSON.stringify(data));
}
