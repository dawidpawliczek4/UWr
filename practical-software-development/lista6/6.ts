// 1. Extract i Exclude
type T = "a" | "b" | "c";
type Extracted = Extract<T, "a" | "b">; // "a" | "b"
type Excluded = Exclude<T, "a">; // "b" | "c"

// 2. Record, Required, Readonly, Partial
// Record
type RecordType = Record<"a" | "b", number>; // { a: number; b: number }

// Required
type OptionalType = { a?: number; b?: string };
type RequiredType = Required<OptionalType>; // { a: number; b: string }

// Readonly
type MutableType = { a: number; b: string };
type ReadonlyType = Readonly<MutableType>; // { readonly a: number; readonly b: string }

// Partial
type FullType = { a: number; b: string };
type PartialType = Partial<FullType>; // { a?: number; b?: string }

// 3. Pick i Omit
// Pick
type PickedType = Pick<FullType, "a" | "b">; // { a: number; b: string }

// Omit
type OmittedType = Omit<FullType, "b">; // { a: number }

// 4. Indexed Access Types
type ObjectType = { a: number; b: string; c: boolean };
type ValueTypeA = ObjectType["a"]; // number
type ValueTypeB = ObjectType["b" | "c"]; // string | boolean

// Przydatność w praktyce:
// Możesz używać tych mechanizmów do operowania na typach dynamicznie, redukując powtarzalność i zwiększając bezpieczeństwo typów.
