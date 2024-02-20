const firebaseConfig = {
    apiKey: "AIzaSyCJNpKxxxIfa9wgkSW9xDYytygfuc7wibY",
    authDomain: "taiyo-768b4.firebaseapp.com",
    projectId: "taiyo-768b4",
    storageBucket: "taiyo-768b4.appspot.com",
    messagingSenderId: "468296642765",
    appId: "1:468296642765:web:a667d8fb3eced631d4b984",
    measurementId: "${config.measurementId}"
};
firebase.initializeApp(firebaseConfig);

var storage = firebase.storage();

var image_link_1 = document.getElementById('id_image_1_link');
var image_link_2 = document.getElementById('id_image_2_link');
var image_link_3 = document.getElementById('id_image_3_link');
var image_link_4 = document.getElementById('id_image_4_link');
var excel_file_link = document.getElementById('id_excel_file_link');
var pdf_file_link = document.getElementById('id_pdf_file_link');

var product = document.getElementById("id_product");
var base_price = document.getElementById("id_basic_price");
var product_description = document.getElementById("id_product_description");

var image_1_id = "id_image_1";
var image_2_id = "id_image_2";
var image_3_id = "id_image_3";
var image_4_id = "id_image_4";

document.getElementsByClassName("field-image_1_link")[0].style.display = "none";
document.getElementsByClassName("field-image_2_link")[0].style.display = "none";
document.getElementsByClassName("field-image_3_link")[0].style.display = "none";
document.getElementsByClassName("field-image_4_link")[0].style.display = "none";

image_link_1.style.display = "none"

document.getElementById("id_image_1").addEventListener("change", () => getFileLink(image_link_1, image_1_id, "image_1_display"))
document.getElementById("id_image_2").addEventListener("change", () => getFileLink(image_link_2, image_2_id, "image_2_display"))
document.getElementById("id_image_3").addEventListener("change", () => getFileLink(image_link_3, image_3_id, "image_3_display"))
document.getElementById("id_image_4").addEventListener("change", () => getFileLink(image_link_4, image_4_id, "image_4_display"))
document.getElementById("id_excel_file").addEventListener("change", () => getFileLink(excel_file_link, "id_excel_file"))
document.getElementById("id_pdf_file").addEventListener("change", () => getFileLink(pdf_file_link, "id_pdf_file"))

const getFileLink = (image_link, image_id, image_display = null) => {
    var storageRef = firebase.storage().ref();
    var file = document.getElementById(image_id).files[0];
    var folder_name = base_price.value + product_description.value;
    var thisRef = storageRef.child(`Advertisements/${folder_name}/${file.name}`);
    
    thisRef.put(file).then((snapshot) => {
        var ref = storage.ref().child(`Advertisements/${folder_name}/${file.name}`);
        ref.getDownloadURL().then((url) => {
            image_link.value = url;
            if (image_display !== null) {
                document.getElementById(image_display).innerHTML = `<img src="${url}" width="auto" height="150px" />`
            }
        }).catch((error) => {
            console.log(error)
            alert("some error occured");
        })
    }).catch((error) => {
        alert("some error occured");
    })
}