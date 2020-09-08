# Modular.im Policy Documents

Documents in this directory describe:
- The Customer's use of the Modular.im admin web interface at https://www.modular.im
- The Customer's relationship to data stored on their hosted homeservers

## How to copy the html from build to EMS
- `npm run build`
- Copy the contents from build/ems to
    - `matrix-hosted/packages/web/pages/cookie_policy.js`
    - `matrix-hosted/packages/web/pages/privacy_policy.js`
    - `matrix-hosted/packages/web/pages/terms_of_service.js`
- ... replacing everything in between `<Container> </Container>`
- Set indentation for the html to zero
- Search and replace `<br>` --> `<br/>` in all three js files
- In `cookie_policy`, replace `<table>` --> `<table className='fancyTable'>`
