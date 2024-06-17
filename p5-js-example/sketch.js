/* disegna una barca di legno con una vela bianca sul mare mare blu 
- il cielo è azzurro con una  nuvola bianca
- la nuvola ha tre cerchi bianchi che si sovrappongono tra loro
- il sole è un cerchio giallo all'interno di un cerchio arancione in alto a destra
- la vela è un grande triangolo bianco connesso a un rettangolo marrone che rappresenta la barca
- la barca è curva e ha una forma di banana rovesciata
*/

function setup() {
  createCanvas(400, 400);
  background(135, 206, 235);
  noLoop();
}

function draw() {
  // cielo
  fill(135, 206, 235);
  rect(0, 0, 400, 300);
  // mare
  fill(0, 0, 205);
  rect(0, 300, 400, 100);
  // sole
  fill(255, 165, 0);
  ellipse(350, 50, 100);
  fill(255, 215, 0);
  ellipse(350, 50, 80);
  // nuvola
  fill(255);
  ellipse(100, 50, 50);
  ellipse(130, 50, 50);
  ellipse(115, 70, 50);
  // barca
  fill(139, 69, 19);
  beginShape();
  vertex(50, 300);
  vertex(50, 200);
  vertex(200, 200);
  vertex(200, 300);
  endShape(CLOSE);
  fill(255);
  triangle(50, 200, 200, 200, 200, 100);
}