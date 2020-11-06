<template>
  <nav>
    <b>York<br />Graffiti<br />Explorer</b>
    <button>menu</button>
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
  width: calc(100% - 2rem);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: var(--darkblue);
  color: var(--red);
  ul {
    position: absolute;
  }
  button {
    border: 1px solid var(--red);
  }
}
</style>