const fs = require("fs");
const { createCanvas, loadImage } = require("canvas");
const Tesseract = require("tesseract.js");

function processImage(imagePath, outputFilePath = null) {
  console.log(`Processing image: ${imagePath}`);

  loadImage(imagePath).then((image) => {
    const canvas = createCanvas(image.width, image.height);
    const ctx = canvas.getContext("2d");
    ctx.drawImage(image, 0, 0);

    Tesseract.recognize(imagePath, "eng")
      .then(({ data: { words } }) => {
        ctx.strokeStyle = "red";
        ctx.lineWidth = 2;

        for (const word of words) {
          const { x0, y0, x1, y1 } = word.bbox;
          ctx.strokeRect(x0, y0, x1 - x0, y1 - y0);
        }

        if (outputFilePath) {
          const out = fs.createWriteStream(outputFilePath);
          const stream = canvas.createPNGStream();
          stream.pipe(out);
          out.on("finish", () =>
            console.log(
              `Output image with bounding boxes saved to ${outputFilePath}`
            )
          );
        } else {
          // Display the image
          const imageBuffer = canvas.toBuffer("image/png");
          fs.writeFileSync("output.png", imageBuffer);
          console.log("Image with bounding boxes saved as output.png");
        }
      })
      .catch((error) => console.error("Error:", error));
  });
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.error("Error: Please provide the path to the input image.");
    process.exit(1);
  }

  const imagePath = args[0];
  const outputFilePath = args.length > 1 ? args[1] : null;

  processImage(imagePath, outputFilePath);

  if (!outputFilePath) {
    console.log("Output file name was not provided. Displaying the image...");
  }
}

if (require.main === module) {
  main();
}
