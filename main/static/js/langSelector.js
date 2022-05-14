const allLang = ['en', 'ru'];

            function changeLanguage() {
            let hash = localStorage.getItem("lng");
            console.log(hash);
            if (!allLang.includes(hash)) {
                location.href = window.location.pathname + '#en';
                location.reload();
            }

            for (let key in langArr) {
                    let elem = document.querySelector('.lng-' + key);
                    if (elem) {
                        elem.innerHTML = langArr[key][hash];
                    }

                }
            }