// function changeColor(imageUrl){
//     const product_image = document.getElementById('currentProduct')
//     product_image.src = imageUrl
// }


function countMoney(operation, money)
{
    let val = document.getElementById('number_of_products_self')
    let price = document.getElementById('final_price')

    if (operation == '+' && val.value > 0)
    {
        val.value = +val.value + 1
        price.textContent = (+val.value * money).toFixed(2)
    }
    else if (operation == '-' && val.value > 1)
    {
        val.value = +val.value - 1
        price.textContent = (+val.value * money).toFixed(2)
    }
    else
    {
        val.value = 1
    }
}


function thanking()
{
    function updateTimer(timerElement, time)
    {
        timerElement.textContent = time
        console.log(time)
    }

    let thanks_block = document.getElementById('thanks-block')
    let timer = document.getElementById('timer')

    thanks_block.style.display = "block"

    // if (language == "en")
    // {
    //     alert("Thank you for your purchase!")
    // }
    // else if(language == "ua")
    // {
    //     alert("Дякую за Вашу покупку!")
    // }

    for (let index = 20; index > 0; index--)
    {
        setTimeout(() => updateTimer(timer, index), (20 - index) * 1000);
    }

    setTimeout(() => {
        thanks_block.style.display = "none";
    }, 20000);
}