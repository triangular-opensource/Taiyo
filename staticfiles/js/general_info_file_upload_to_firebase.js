var storage = firebase.storage();

var icon_link = document.getElementById('id_icon_link');
var cover_link = document.getElementById('id_cover_image_link');

document.getElementsByClassName("field-icon_link")[0].style.display = "none";
document.getElementsByClassName("field-cover_image_link")[0].style.display = "none";

document.getElementById("id_icon").addEventListener("change", () => getTaiyoFileLink(icon_link, "id_icon", "icon_display"))
document.getElementById("id_cover_image").addEventListener("change", () => getTaiyoFileLink(cover_link, "id_cover_image", "cover_display"))

const getTaiyoFileLink = (image_link, image_id, image_display = null) => {
    var storageRef = firebase.storage().ref();
    var file = document.getElementById(image_id).files[0];
    var thisRef = storageRef.child(`Taiyo/${file.name}`);
    
    thisRef.put(file).then((snapshot) => {
        var ref = storage.ref().child(`Taiyo/${file.name}`);
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
