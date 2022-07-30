function myFunction() {
  if (document.getElementsByClassName('hamburger-responsive').length == 0) {
        var nbItems = document.getElementsByClassName('nav-bar__items');
        for (var i = 0, length = nbItems.length; i < length; i++) {
        nbItems[i].style.display = 'block';
        }

        var navBar = document.getElementsByClassName('nav-bar');
        for (var i = 0, length = navBar.length; i < length; i++) {
        navBar[i].style.height = '100vh';
        navBar[i].style.flexDirection = 'column';
        navBar[i].style.justifyContent = 'center';
        navBar[i].style.verticalAlign = 'center';
        }

        var nbItem = document.getElementsByClassName('nav-bar__item');
        for (var i = 0, length = nbItem.length; i < length; i++) {
        nbItem[i].style.display = 'block';
        nbItem[i].style.justifyContent = 'center';
        nbItem[i].style.textAlign = 'center';
        }

        var nbBrand = document.getElementsByClassName('nav-bar__brand');
        for (var i = 0, length = nbBrand.length; i < length; i++) {
        nbBrand[i].style.display = 'none';
        }

        var hbResponse = document.getElementsByClassName('toggle-button');
        hbResponse[0].classList.add('hamburger-responsive');
  }
 else {
        var nbItems = document.getElementsByClassName('nav-bar__items');
        for (var i = 0, length = nbItems.length; i < length; i++) {
        nbItems[i].style.display = 'none';
        }

        var navBar = document.getElementsByClassName('nav-bar');
        for (var i = 0, length = navBar.length; i < length; i++) {
        navBar[i].style.height = '5rem';
        navBar[i].style.flexDirection = 'row';
        navBar[i].style.justifyContent = 'flex-start';
        navBar[i].style.alignItems = 'center';
        }

        var nbItem = document.getElementsByClassName('nav-bar__item');
        for (var i = 0, length = nbItem.length; i < length; i++) {
        nbItem[i].style.display = 'inline-block';
        }

        var nbBrand = document.getElementsByClassName('nav-bar__brand');
        for (var i = 0, length = nbBrand.length; i < length; i++) {
        nbBrand[i].style.display = 'block';
        }

        var hbResponse = document.getElementsByClassName('toggle-button');
        hbResponse[0].classList.remove('hamburger-responsive');


 }
}