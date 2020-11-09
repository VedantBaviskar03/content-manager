<template>
    <div class="input-new-entry">
        <div class="input-container">
            Name <input v-model="enteredName" type="text" id="name">
            Username <input v-model="enteredUser" type="text" id="username">
            Email <input v-model="enteredMail" type="text" id="email">
            URL <input v-model="enteredUrl" type="text" id="url">
            Tags <input v-model="enteredTags" type="text" id="tags">
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
            enteredName: "",
            enteredUser: "",
            enteredMail: "",
            enteredUrl: "",
            enteredTags: ""
        }
    },
    methods: {
        emitEntered: function() {
            this.$emit("entered");
        },
        enterContent: async function() {
            await fetch(this.endpoint, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "name": this.enteredName,
                    "username": this.enteredUser,
                    "email": this.enteredMail,
                    "url": this.enteredUrl,
                    "tags": this.enteredTags, 
                })
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