counter = 0

function changeItemNext(list1, list2, list3){
    let name = document.getElementById('nameOfNews')
    let desc = document.getElementById('descriptionOfNews')
    let photo = document.getElementById('photoOfNews')
    let link = document.getElementById('linkOfNews')

    if (counter == 2){
        counter = 0
    }
    else{
        counter += 1        
    }

    if (counter == 0){
        photo.src = "./../" + list1[0]
        name.textContent = list1[1]
        desc.textContent = (list1[2] + "...")
        link.href = list1[3]
    }
    else if (counter == 1){
        photo.src = "./../" + list2[0]
        name.textContent = list2[1]
        desc.textContent = (list2[2] + "...")
        link.href = list2[3]
    }
    else if (counter == 2){
        photo.src = "./../" + list3[0]
        name.textContent = list3[1]
        desc.textContent = (list3[2] + "...")
        link.href = list3[3]
    }
    console.log(counter)
}


function changeItemPrevious(list1, list2, list3){
    let name = document.getElementById('nameOfNews')
    let desc = document.getElementById('descriptionOfNews')
    let photo = document.getElementById('photoOfNews')
    let link = document.getElementById('linkOfNews')

    if (counter == 0){
        counter = 2
    }
    else{
        counter -= 1        
    }

    if (counter == 0){
        photo.src = "./../" + list1[0]
        name.textContent = list1[1]
        desc.textContent = (list1[2] + "...")
        link.href = list1[3]
    }
    else if (counter == 1){
        photo.src = "./../" + list2[0]
        name.textContent = list2[1]
        desc.textContent = (list2[2] + "...")
        link.href = list2[3]
    }
    else if (counter == 2){
        photo.src = "./../" + list3[0]
        name.textContent = list3[1]
        desc.textContent = (list3[2] + "...")
        link.href = list3[3]
    }
    console.log(counter)
}