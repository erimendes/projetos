document.addEventListener('DOMContentLoaded', function() {
  const searchIcon = document.querySelector('.busca__icone');
  const searchContainer = document.querySelector('.busca__fundo');

  searchIcon.addEventListener('click', function() {
      if (searchContainer.style.display === 'none' || !searchContainer.style.display) {
          searchContainer.style.display = 'flex';
      } else {
          searchContainer.style.display = 'none';
      }
  });
});
