// flatmate url cekmek icin
let urls = [];
aList = document.querySelectorAll("a");
aList.forEach(a => {
    let idMatch = a.id.match(/^.*?-.*?-.*?-.*?-.*?-\S+/);
    if(idMatch!=null) urls.push(a.href);
});


// ayni url varsa silmek icin
let urlClean = [];
for(let i = 0; i<urls.length-1; i++){
    let flag = 0;
    for (let j = i+1; j < urls.length; j++) {
        if(urls[i]==urls[j]) flag = 1;  
    }
    if(flag == 0) urlClean.push(urls[i]);
}


