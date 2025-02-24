from auth import router as AuthRouter

# Define routes


def register_routes(app):
    app.include_router(AuthRouter)
