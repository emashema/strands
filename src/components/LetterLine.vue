<template>
    <svg
        :class="{
            'line': true,
            'in-spangram': in_spangram
        }"
    >
        <line
            :x1="(y1*53.5)+22"
            :y1="(x1*51)+17"
            :x2="(y2*53.5)+22"
            :y2="(x2*51)+17"
            stroke-width="10px"
        />
    </svg>
</template>

<script>
export default {
    props: [ "x1", "y1", "x2", "y2" ],
    data() {
        return {
            in_spangram: false
        }
    }
}
</script>