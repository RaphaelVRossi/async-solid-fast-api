import uvicorn


def main():
    uvicorn.run(
        "async_solid_fast_api.core.app:app",
    )


if __name__ == "__main__":
    main()
