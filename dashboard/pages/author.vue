<template>
    <section class="section">
        <b-row class="mb-2 justify-center">
            <b-form-input v-model="keyword" placeholder="Enter your name" class="mr-2"></b-form-input>
            <b-button v-b-modal.modal-author variant="danger">Add new author</b-button>
        </b-row>
    
        <b-row>
            <b-table striped hover :items="items" :busy="isBusy" select-mode="single" selectable outlined @row-selected="onRowSelected">
                <template #table-busy>
              <div class="text-center text-danger my-2">
                <b-spinner class="align-middle"></b-spinner>
                <strong>Loading...</strong>
              </div>
</template>
      </b-table>
      <Pagination :page-count=pageNumbers :page-number=currentPage />
    </b-row>
    <AuthorModal :author="selected" />
  </section>
</template>

<script lang="ts">
import Pagination from "~/components/Pagination.vue"
import { AuthorRow, BookRow } from "~/types/base"
import { AuthorResponse } from "~/types/interface"


export default {
    components: {
        Pagination
    },
    data() {
        return {
            selected: -1,
            pageNumbers: 5,
            pageNumberCount: 10,
            currentPage: 1,
            isBusy: true,
            items: [],
            keyword: ''
        }
    },
    async created() {
        try {
            const res: AuthorResponse = (await this.$axios.post("/authors", {
                item_count: this.pageNumberCount,
                page_number: 0
            }));
            this.isBusy = true
            console.log('author', JSON.stringify(res))
            this.pageNumbers = res.pageCount
            this.items = res.list
        } catch (e) {

        }
    },
    methods: {
        onRowSelected(items: BookRow) {
            // this.selected = items
            // this.$refs['modal-author'].show()
        },
    }

}
</script>