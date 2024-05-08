<template>
    <div
        :class="{'h4': true, 'letter': true, 'cursor-pointer': true, 'selected': selected}"
        @click="click"
    >
        {{ letter }}
    </div>
</template>

<script>
export default {
    props: {
        "letter": {
            type: String,
            required: true
        },
    },
    data() {
        return {
            selected: false
        }
    },
    methods: {
        click() {
            this.selected = !this.selected;
            this.$emit('select');
        }
    }
}
</script>