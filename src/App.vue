<template>
  <div id="app">
    <router-link class="linkLogo" id="ecLogo" to="/">
      <img src="@/assets/electron_cloud.svg">
    </router-link>
    <div id="header">
    </div>
    <div id="nav-background"/>
    <div id="nav">
      <router-link class="linkLogo" to="/collection">
        <!-- <img src="@/assets/vue-logo.png"> -->
        <p>Collection</p>
      </router-link>
      <router-link class="linkLogo" to="/portfolio">
        <!-- <img src="@/assets/vue-logo.png"> -->
        <p>Portfolio</p>
      </router-link>
    </div>
  </div>
</template>

<script>
import NavLink from '@/components/NavLink.vue'
require('./assets/vue-logo.png')
export default {
  components: {
    NavLink
  }
}
</script>

<style lang="scss">
#ecLogo {
  width: 70px;
  position: absolute;
  padding: 12px 0px 0 41px;
  z-index: 10;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #97B17F;
  display: flex;
  background-color: #80808030;
}
#header {
  height: 70px;
  width: 100vw;
  background-color: white;
  position: absolute;
}
#nav-background {
  background-color: #E6CABD;
  height: 100vh;
  opacity: 0.8;
  width: 150px;
}
#nav {
  position: relative;
  top: 150px;
  right: 150px;
  width: 150px;
  .linkLogo {
    opacity: 1;
    display: flex;
    flex-direction: column;
    p {
      font-weight: bold;
      color: #FFFFFF;
      margin: auto;
    }
  }
  a {
    text-decoration: none;
    font-weight: bold;
    color: #FFFFFF;
    margin: auto;
    &.router-link-exact-active {
      p {
        color: #97B17F;
      }
    }
  }
}

</style>
