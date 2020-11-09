<template>
    <div class="delete-container">
        <h2>Delete content</h2>
        Name <input v-model="nameEntered">
        <button @click="deleteUpstream">Delete content</button>
    </div>
</template>

<script>
export default {
    name: "Delete",
    data() {
        return {
            nameEntered: "",
            endpoint: "http://localhost:5000/"
        }
    },
    methods: {
        deleteUpstream: async function() {
            const response = await fetch(`${this.endpoint}?${new URLSearchParams({
                'name': this.nameEntered
            })}`, {
                method: "DELETE"
            });
            if (response.status != 200) {
                alert("Something went wrong while trying to delete");
            }

            // Else it must've been deleted
            this.$emit("deleted");
            this.nameEntered = ""
        }
    }
}
</script>

<style lang="scss" scoped>
input {
    display: block;
    margin-top: 10px;
}
button {
    margin-top: 20px;
}
</style>