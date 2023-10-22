import { AuthorRow } from "./base";

export type AuthorResponse = {
    pageCount: number;
    list: Array<AuthorRow>;
}
