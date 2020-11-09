<template>
  <div id="app">
    <div class="left-container">
      <InputEntry @entered="refreshContent" />
      <Delete @deleted="refreshContent" />
    </div>
    <div class="right-container">
      <Entries ref="entryContainer" class="entries-container__parent" />
    </div>
  </div>
</template>

<script>
import Entries from "@/components/Entries";
import InputEntry from "@/components/Input";
import Delete from "@/components/Delete";

export default {
  name: "App",
  components: {
    Entries,
    InputEntry,
    Delete
  },
  methods: {
    refreshContent: function() {
      this.$refs.entryContainer.fetchUpstream();
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

  display: flex;
  justify-content: center;
  width: 80%;
  margin: 0 auto;
  padding: 2.5em 0;

  .left-container, .right-container {
    width: 50%;
  }

  .entries-container__parent {
    width: 50%;
    border: 1px solid grey;
    padding: 1em 2em;
  }
}
</style>
