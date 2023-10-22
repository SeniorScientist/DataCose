export type BookRow = {
    id: Number;
    name: string;
    authorName: string;
    pageNumber: Number;
}

export type AuthorRow = {
    id: Number;
    name: string;
    books: Array<BookRow>
}
