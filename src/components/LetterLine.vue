<template>
    <svg
        class="line"
    >
        <line
            :x1="(x1*45)+22"
            :y1="(y1*43)+17"
            :x2="(x2*45)+22"
            :y2="(y2*43)+17"
            stroke="greenyellow"
            stroke-width="10px"
        />
    </svg>
</template>

<script>
export default {
    props: [ "x1", "y1", "x2", "y2" ]
}
</script>