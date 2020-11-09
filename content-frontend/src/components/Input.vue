<template>
    <div class="input-new-entry">
        <div class="input-container">
            Name <input v-model="data.name" type="text" id="name">
            Username <input v-model="data.username" type="text" id="username">
            Email <input v-model="data.email" type="text" id="email">
            URL <input v-model="data.url" type="text" id="url">
            Tags <input v-model="data.tags" type="text" id="tags">
        </div>
        <button @click="enterContent">Add content</button>
    </div>
</template>

<script>
export default {
    name: "InputEntry",
    data() {
        return {
            endpoint: "http://localhost:5000/",
            data: {
                name: "",
                username: "",
                email: "",
                url: "",
                tags: ""
            }
        }
    },
    methods: {
        emitEntered: function() {
            this.$emit("entered");
            
            // Clear all the data in the data object
            for (let key in this.data) {
                this.data[key] = ""
            }
        },
        enterContent: async function() {
            await fetch(this.endpoint, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(this.data)
            });
            this.emitEntered();
        }
    }
}
</script>

<style lang="scss" scoped>
.input-new-entry {
    .input-container {
        padding: 1em;
        input {
            display: block;
            margin-bottom: 0.5em;
        }
    }
}
</style>