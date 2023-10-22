<template>
    <div class="overflow-auto">
        <b-pagination-nav :link-gen="linkGen" :number-of-pages="pageCount" use-router></b-pagination-nav>
    </div>
</template>
  
<script>
export default {
    name: 'Pagination',
    props: {
        pageCount: {
            type: Number,
            default: 1
        },
        pageNumber: {
            type: Number,
            default: 0
        }
    },
    methods: {
        linkGen(pageNum) {
            return pageNum === 1 ? '?' : `?page=${pageNum}`
        }
    },
    // computed: {
        
    // }
}
</script>
  