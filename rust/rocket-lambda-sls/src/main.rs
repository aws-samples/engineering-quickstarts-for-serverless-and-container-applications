#![warn(missing_docs)]
//! Cart Crate
//!
use std::*;
use rocket::{routes, get, post, catch, catchers, delete};
use rocket::serde::json::{Json, Value, json};
use rocket::serde::{Serialize, Deserialize};
use lambda_web::{is_running_on_lambda, launch_rocket_on_lambda, LambdaError};
use opentelemetry::{
    global,
    sdk::export::trace::stdout,
    sdk::trace as sdktrace,
    trace::{TraceContextExt, Tracer},
    Context, KeyValue
};
use opentelemetry_aws::XrayPropagator;
use opentelemetry_http::HeaderInjector;

#[derive(Serialize, Deserialize)]
#[serde(crate = "rocket::serde")]
struct Item {
    pk: String,
    sk: String,
    name: String,
}

/// Add item to cart
/// Payload expected [`AddItem`](AddItem)
/// Adds provided Item to the cart
#[post("/add", format="json", data="<payload>")]
async fn add(payload: Json<AddItem<>>) -> Value {
    let item_added: Option<AddItem> = None;

    json!(item_added)
}

/// Search Items in the Cart
/// Payload expected [`SearchItem`](SearchItem)
/// Search for a search term among current cart items
#[post("/search", format="json", data="<payload>")]
async fn search(payload: Json<SearchCart<>>) -> Value {
    let found_items: Option<SearchCart> = None;

    json!(found_items)
}

/// Move Items from wishlist to cart
/// Payload expected [`MoveWishlistToCart`](MoveWishlistToCart)
/// Move all items from wishlist to cart
#[post("/move_to_cart", format="json", data="<payload>")]
async fn move_to_cart(payload: Json<MoveWishlistToCart<>>) -> Value {
    let cleared_wishlist: Option<MoveWishlistToCart> = None;

    json!(cleared_wishlist)
}

/// Clear items in cart
/// Empty's the cart and returns all removed items
#[delete("/clear")]
async fn clear() -> Value {

    json!("None")
}



#[catch(404)]
async fn not_found() -> Value {
    json!({
        "status": "error",
        "reason": "Resource was not found."
    })
}

#[rocket::main]
async fn main() -> std::result::Result<(), LambdaError> {
    let rocket = rocket::build()
        .mount("/", routes![])
        .register("/", catchers![not_found]);
    if is_running_on_lambda() {
        // Launch on AWS Lambda
        launch_rocket_on_lambda(rocket).await?;
    } else {
        // Launch local server
        let _ = rocket.launch().await?;
    }
    Ok(())
}

