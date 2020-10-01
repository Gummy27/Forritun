const canvas = document.getElementById("tutorial");
const ctx = canvas.getContext("2d");

const width  = canvas.width  = window.innerWidth;
const height = canvas.height = window.innerHeight;

function random(min, max) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min
    return num
}

class Shape{
    constructor(x, y, velX, velY, color, size) {
        this.x = x;
        this.y = y;
        this.velX = velX;
        this.velY = velY;
        this.color = color;
        this.size = size;   
    }

    draw() {
        ctx.beginPath();
        ctx.moveTo(this.x + this.size * Math.cos(0), this.y + this.size * Math.sin(0));

        for (let side = 0; side < 7; side++) {
            ctx.lineTo(this.x + this.size * Math.cos(side * 2 * Math.PI / 6), this.y + this.size * Math.sin(side * 2 * Math.PI / 6));
        }

        ctx.fillStyle = this.color;
        ctx.fill();
    }

    update() {
        if ((this.x + this.size) >= width) {
            this.velX = -(this.velX);
          }
        
          if ((this.x - this.size) <= 0) {
            this.velX = -(this.velX);
          }
        
          if ((this.y + this.size) >= height) {
            this.velY = -(this.velY);
          }
        
          if ((this.y - this.size) <= 0) {
            this.velY = -(this.velY);
          }
        
          this.x += this.velX;
          this.y += this.velY;
    }

    collisionDetect() {
        for (let j = 0; j < goodShapes.length; j++) {
            if (!(this === goodShapes[j])) {
                const dx = this.x - goodShapes[j].x;
                const dy = this.y - goodShapes[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + goodShapes[j].size) {
                    goodShapes[j].color = this.color = 'rgb(' + random(0, 255) + ',' + random(0, 255) + ',' + random(0, 255) +')';
                }
            }
        }
    }

}

class EvilShape extends Shape {
    constructor(x, y, velX, velY) {
        super(x, y, velX, velY, "white", 10);
        this.exists = true;
    }

    draw() {
        ctx.beginPath();
        ctx.moveTo(this.x + this.size * Math.cos(0), this.y + this.size * Math.sin(0));

        for (let side = 0; side < 7; side++) {
            ctx.lineTo(this.x + this.size * Math.cos(side * 2 * Math.PI / 6), this.y + this.size * Math.sin(side * 2 * Math.PI / 6));
        }

        ctx.strokeStyle = this.color;
        ctx.stroke();
    }

    collisionDetect() {
        if(this.exists) {
            for (let j = 0; j < goodShapes.length; j++) {
                if (!(this === goodShapes[j])) {
                    const dx = this.x - goodShapes[j].x;
                    const dy = this.y - goodShapes[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < this.size + goodShapes[j].size) {
                        this.velX += 4;
                        this.velY += 4;
                        goodShapes[j].killed(j);
                        j--;
                    }
                }
            }
        }
    }
}

class GoodShape extends Shape {
    constructor(x, y, velX, velY, color, size, alive) {
        super(x, y, velX, velY, color, size);
        this.alive = true;
    }

    killed(index) {
        this.alive = false;
        goodShapes.splice(index, 1);
        this.color = "black";
    }
}


let goodShapes = [];

while (goodShapes.length < 25) {
    let size = random(10, 20);
    let shape = new GoodShape(
        random(0 + size,width - size),
        random(0 + size,height - size),
        random(-7,7),
        random(-7,7),
        'rgb(' + random(0,255) + ',' + random(0,255) + ',' + random(0,255) +')',
        size
    );

    goodShapes.push(shape)
}

let evilShapes = [];
while (evilShapes.length < 2) {
    let evilShape = new EvilShape(
        random(0 + 10 ,width - 10),
        random(0 + 10 ,height - 10),
        random(-7,7),
        random(-7,7),
        true
    )

    evilShapes.push(evilShape);
}

function loop() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.25)';
    ctx.fillRect(0, 0, width, height);
  
    for (let i = 0; i < goodShapes.length; i++) {
      goodShapes[i].draw();
      goodShapes[i].update();
      goodShapes[i].collisionDetect();
    }

    for (let i = 0; i < evilShapes.length; i++) {
        evilShapes[i].draw();
        evilShapes[i].update();
        evilShapes[i].collisionDetect();
      }

    requestAnimationFrame(loop);
}

loop();