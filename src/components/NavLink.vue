<template>
  <div class="link">
    <img :src=logo>
    <router-link :to=link>{{label}}</router-link> |
  </div>
</template>

<script>
export default {
  name: 'NavLink',
  props: {
    logo: String,
    link: String,
    label: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.link {
  display: flex;
  flex-direction: column;
  a {
    font-weight: bold;
    color: #FFFFFF;
    margin: auto;
    &.router-link-exact-active {
      color: #97B17F;
    }
  }
}
</style>
