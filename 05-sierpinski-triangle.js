var canvasWidth = 600;
var canvasHeight = 600;
var level = 8;

function setup() {
  createCanvas(canvasWidth, canvasHeight);
  noLoop();
}

function getMidpoint(p1, p2) {
  return createVector((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
}

function getRandomColor() {
  return color(random(100, 150), random(100, 200), random(100, 255))
}

function drawTriangle(p1, p2, p3) {
  noStroke()
  fill(getRandomColor())
  triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
}

class Triangle {
  constructor(p1, p2, p3) {
    this.p1 = p1;
    this.p2 = p2;
    this.p3 = p3;
  }
  
  draw() {
    drawTriangle(this.p1, this.p2, this.p3)
  }
}

function drawSierpinskiTriangle(tri, depth) {
  if (depth === level) {
    return
  }

  let m1 = getMidpoint(tri.p1, tri.p2)
  let m2 = getMidpoint(tri.p2, tri.p3)
  let m3 = getMidpoint(tri.p3, tri.p1)
  let tri_0 = new Triangle(m1, m2, m3)
  tri_0.draw()
  
  drawSierpinskiTriangle(new Triangle(tri.p1, m1, m3), depth + 1)
  drawSierpinskiTriangle(new Triangle(tri.p2, m2, m1), depth + 1)
  drawSierpinskiTriangle(new Triangle(tri.p3, m3, m2), depth + 1)
}

function draw() {
  background(250);
  let p1 = createVector(canvasWidth/2, 0)
  let p2 = createVector(0, canvasHeight)
  let p3 = createVector(canvasWidth, canvasHeight)
  let tri_0 = new Triangle(p1, p2, p3)
  tri_0.draw()
  drawSierpinskiTriangle(tri_0, 0)
}
