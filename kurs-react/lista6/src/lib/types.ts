export type ProductType = {
  id: number;
  name: string;
  type: number;
  price: number;
  availability: boolean;
  quantity: number;
};

export type SortBy =
  | "name"
  | "type"
  | "price"
  | "availability"
  | "quantity"
  | "none";