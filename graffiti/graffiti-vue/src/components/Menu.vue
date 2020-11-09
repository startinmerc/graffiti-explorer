<template>
  <nav>
    <p id="nav-logo"><router-link to="/">York<br />Graffiti<br />Explorer</router-link></p>
    <router-link to="/about"><button>menu</button></router-link>
  </nav>
</template>

<script>
export default {
  name: "Menu"
}
</script>

<style lang="scss">
nav {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 100;
  width: calc(100% - 2rem);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: var(--darkblue);
  color: var(--red);
  #nav-logo {
    margin:0;
  }
  #nav-logo * {
    color: var(--red);
    text-decoration: none;
  }
  ul {
    position: absolute;
  }
  button {
    border: 1px solid var(--red);
  }
}
</style>