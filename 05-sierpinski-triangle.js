var canvasWidth = 600;
var canvasHeight = 600;
var level = 10;

function setup() {
  createCanvas(canvasWidth, canvasHeight);
  noLoop();
}

function getRandomColor() {
  return color(
    random(0, 255),
    random(0, 255),
    random(0, 255),
  )
}

function drawTriangle(p1, p2, p3) {
  fill(getRandomColor())
  triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
}

function getMidpoint(p1, p2) {
  return createVector((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
}

class Triangle {
  constructor(p1, p2, p3) {
    this.p1 = p1
    this.p2 = p2
    this.p3 = p3
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

  let t0 = new Triangle(m1, m2, m3)
  t0.draw()

  let t1 = new Triangle(tri.p1, m1, m3)
  let t2 = new Triangle(tri.p2, m1, m2)
  let t3 = new Triangle(tri.p3, m2, m3)

  drawSierpinskiTriangle(t1, depth + 1)
  drawSierpinskiTriangle(t2, depth + 1)
  drawSierpinskiTriangle(t3, depth + 1)
}

function draw() {
  background(250);
  let p1 = createVector(canvasWidth / 2, 0)
  let p2 = createVector(0, canvasHeight)
  let p3 = createVector(canvasWidth, canvasHeight)

  let t1 = new Triangle(p1, p2, p3)
  t1.draw()

  drawSierpinskiTriangle(t1, 0)
}
