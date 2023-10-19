export type BookRow = {
    name: string;
    authorName: string;
    pageNumber: Number;
}

export type AuthorRow = {
    name: string;
    books: Array<BookRow>
}
