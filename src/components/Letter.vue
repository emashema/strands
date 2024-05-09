<template>
    <div
        :class="{
            'h4': true,
            'letter': true,
            'cursor-pointer': true,
            'hinted': hinted,
            'selected': (selected || in_solved),
            'in-spangram': in_spangram
        }"
        :key="letter+'-'+selected"
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
        }
    },
    data() {
        return {
            hinted: false,
            selected: false,
            in_solved: false,
            in_spangram: false
        }
    },
    methods: {
        click() {
            // Do not register click if letter is part of an already solved word
            if(this.in_solved == false)

                // First click
                if(this.selected == false) {
                    this.selected = true;
                    this.$emit('click');
                }

                // Second click
                else
                    this.$emit('submit');
        }
    }
}
</script>