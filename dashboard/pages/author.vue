<template>
    <section class="section">
        <b-container>
            <b-row>
                <b-col cols="4">
                    <b-form-input v-model="keyword" placeholder="Enter your name"></b-form-input>
                </b-col>
                <b-col>
                    <b-button variant="danger">Add new author</b-button>
                </b-col>
            </b-row>

            <b-row>
                <b-table 
                  striped 
                  hover 
                  :items="items" 
                  :busy="isBusy" 
                  select-mode="single" 
                  selectable
                  outlined
                  @row-selected="onRowSelected" >
                    <template #table-busy>
                        <div class="text-center text-danger my-2">
                            <b-spinner class="align-middle"></b-spinner>
                            <strong>Loading...</strong>
                        </div>
                    </template>
                </b-table>
                <Pagination :page-count=pageCount :page-number=pageNumber />
            </b-row>
            <b-button v-b-modal.modal-prevent-closing>Open Modal</b-button>
            <AuthorModal />
        </b-container>
    </section>
</template>

<script lang="ts">
import Pagination from "~/components/Pagination.vue"
import { BookRow } from "~/types/base"

export default {
    components: {
        Pagination
    },
    data() {
        return {
            selected: {},
            pageCount: 5,
            pageNumber: 1,
            isBusy: false,
            items: [
                { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
                { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
                { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
                { age: 38, first_name: 'Jami', last_name: 'Carney' }
            ],
            keyword: ''
        }
    },
    methods: {
        onRowSelected(items: BookRow) {
            this.selected = items
        },
    }
}
</script>