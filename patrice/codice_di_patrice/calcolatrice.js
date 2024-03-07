//Project 2 calculatrice

//creer mes fonctions

//fonction pour additionner
function addition(nombreA, nombreB) {
    return nombreA + nombreB
  }
  
  //fonction pour multiplier
  function multiplication(nombreA, nombreB) {
    return nombreA * nombreB
  }
  
  //fonction pour soustraire
  function soustraction(nombreA, nombreB) {
    return nombreA - nombreB
  }
  
  //fonction pour diviser
  function division(nombreA, nombreB) {
    if (nombreB == 0) {
      throw new error('impossible de diviser un nombre par 0')
    }
    return nombreA / nombreB
  }
  
  let restart = false;
  do {
  
    do {
      var choix = Number(prompt('que souhaitez-vous faire? \n\n1-Addition \n2-soustraction \n3-multiplication \n4-division'))
    } while (choix != 1 && choix != 2 && choix != 3 && choix != 4); 4
  
    do {
      var premierNombre = Number(prompt('entrer le premier nombre'));
      var deuxiemeNombre = Number(prompt('enter le deuxieme nombre'));
    }
    while (isNaN(premierNombre) || isNaN(deuxiemeNombre))
  
    try {
      switch (choix) {
        case 1:
          var resultat = addition(premierNombre, deuxiemeNombre)
          break;
  
        case 2:
          var resultat = multiplication(premierNombre, deuxiemeNombre)
          break;
  
        case 3:
          var resultat = soustraction(premierNombre, deuxiemeNombre)
          break;
  
        case 4:
          var resultat = division(premierNombre, deuxiemeNombre)
          break;
        default:
          throw new error('une erreur est survenue dans une alerte. Nous ne sommes jamais à l\'abri d\'un bug.inserer correctemnet les valeurs demandées')
      }
      alert('voici le resultat  : ' + resultat)
    } catch (error) {
      alert(error)
    }
  
    restart = confirm("Souhaitez-vous recommencer un calcul ?"); // On demande grâce à la boîte de dialogue confirm() si l'utilisateur veut recommencer
    alert(restart)
  }
  while (restart)