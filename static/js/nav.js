let dropdowns = document.querySelectorAll('.dropdown-toggle')
        dropdowns.forEach((dd) => {
            dd.addEventListener('click', function(e) {
                var el = this.nextElementSibling
                el.style.display = el.style.display === 'block' ? 'none' : 'block'
                el.classList.toggle('show');
                el.classList.toggle('open');

                // hide other dropdowns
                
            })
        })
        //  #TODO add REFERENCES https://www.codeply.com/p/rhCuZhEUrk 

        


