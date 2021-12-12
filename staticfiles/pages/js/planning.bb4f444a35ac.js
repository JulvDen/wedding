var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var x = c.width/2
var h = c.height

ctx.beginPath();
ctx.moveTo(x, 0);
ctx.lineTo(x, h/5);
ctx.lineTo(x + x/1.5, h/5);
ctx.lineTo(x, h/5);
ctx.lineTo(x, h/2.5);
ctx.lineTo(x - x/1.5, h/2.5);
ctx.lineTo(x, h/2.5);
ctx.lineTo(x, h/1.6667);
ctx.lineTo(x + x/1.5, h/1.6667);
ctx.lineTo(x, h/1.6667);
ctx.lineTo(x, h/1.25);
ctx.lineTo(x - x/1.5, h/1.25);
ctx.lineTo(x, h/1.25);
ctx.lineTo(x, h);
ctx.lineWidth = 2
ctx.stroke();


//ctx.fillRect(x-2.5, 0, 5, 5);
ctx.fillRect(x + x/1.5, h/5 - 2.5, 5, 5);
ctx.fillRect(x - x/1.5, h/2.5 - 2.5, 5, 5);
ctx.fillRect(x - x/1.5, h/1.25 - 2.5, 5, 5);
ctx.fillRect(x + x/1.5, h/1.6667 - 2.5, 5, 5);
//ctx.fillRect(x-2.5, h-5, 5, 5);

ctx.font = '25px serif';

ctx.textAlign = 'end';
ctx.fillText('15:30', c.width, h/5 + 6.25);

ctx.textAlign = 'left';
ctx.fillText('We do', x+x/5, h/5 - 12.5)

ctx.textAlign = 'start';
ctx.fillText('17:00', 0, h/2.5 + 6.25);

ctx.textAlign = 'right';
ctx.fillText('We drink', x-x/5, h/2.5 - 12.5)

ctx.textAlign = 'end';
ctx.fillText('19:30', c.width, h/1.667 + 6.25);

ctx.textAlign = 'left';
ctx.fillText('We eat', x+x/5, h/1.667 - 12.5)

ctx.textAlign = 'start';
ctx.fillText('23:00', 0, h/1.25 + 6.25);

ctx.textAlign = 'right';
ctx.fillText('We party', x-x/5, h/1.25 - 12.5)

window.onload = function() {
	const paar = document.getElementById('paar');
	const glazen = document.getElementById('glazen');
	const eten = document.getElementById('eten');
	const party = document.getElementById('party');
   ctx.drawImage(paar, x-x/5, h/5 - 40, 80, 80);
   ctx.drawImage(glazen, x+x/5 - 80, h/2.5 - 40, 80, 80);
   ctx.drawImage(eten, x-x/5 - 10, h/1.6667 - 40, 80, 80);
   ctx.drawImage(party, x+x/5 - 70, h/1.25 - 40, 80, 80);
   
};