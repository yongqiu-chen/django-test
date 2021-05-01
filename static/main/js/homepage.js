function iniEvent() {
    let list1 = ['select1', 'select2', 'select3']
    let demos = ['demo','demo1','demo2']

    for (const elem of demos) {
        const t = document.getElementById(elem);
        t.onclick = function() {
            for (const elem of list1) {
                const ul = document.getElementById(elem);
                const lis = ul.getElementsByTagName("li");
                for (let i = 0; i < lis.length; i++) {
                    lis[i].removeAttribute("class");
                }
            }
        }
    }
    for (const elem of list1) {
        const ul = document.getElementById(elem);
        const lis = ul.getElementsByTagName("li");
        for (let i = 0; i < lis.length; i++) {
            lis[i].onclick = function () {
                const ul = document.getElementById(elem);
                const lis = ul.getElementsByTagName("li");
                for (let i = 0; i < lis.length; i++) {
                    const li = lis[i];
                    if (li === this) {
                        li.setAttribute("class","left-li-color");
                    }
                    else {
                        if (li.getAttribute("class") === 'left-li-color'){
                            li.removeAttribute("class");
                        }
                    }
               }
            }
        }
    }
}