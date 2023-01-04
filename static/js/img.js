const img_input = document.querySelector("#img-input");

img_input.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector(
      "#display-image"
    ).style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
});

const img_input_pak = document.querySelector("#img-input-pak");
img_input_pak.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_img = reader.result;
    document.querySelector(
      "#display-image-pak"
    ).style.backgroundImage = `url(${uploaded_img})`;
  });
  reader.readAsDataURL(this.files[0]);
});
