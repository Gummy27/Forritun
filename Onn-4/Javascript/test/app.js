var canvas = document.getElementById("tutorial");
var ctx = canvas.getContext("2d");

let x = 0;
let y = 0;
let size = 10;

ctx.beginPath();
ctx.moveTo(x + size * Math.cos(0), y + size * Math.sin(0));

for (let side = 0; side < 7; side++) {
  ctx.lineTo(x + size * Math.cos(side * 2 * Math.PI / 6), y + size * Math.sin(side * 2 * Math.PI / 6));
}

ctx.fillStyle = "#333333";
ctx.fill();