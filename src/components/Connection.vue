<template>
    <svg
        class="line"
    >
        <line
            :x1="x1"
            :y1="y1"
            :x2="x2"
            :y2="y2"
            stroke="yellow"
            stroke-width="10px"
        />
    </svg>
</template>

<script>
export default {
    props: [ "x1", "y1", "x2", "y2" ]
}
</script>