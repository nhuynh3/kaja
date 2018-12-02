<template>
  <div class="ui centered card">
    <h1 class="ui header">Data Input</h1>

<input type="radio" value="One" v-model="picked">
<input type="radio" value="Two" v-model="picked">
<span>Picked: {{ picked }}</span>

  </div>
</template>
