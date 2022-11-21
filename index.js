import * as IPFS from 'ipfs-core';

async function main() {
  const node = await IPFS.create();
  const version = await node.version();

  console.log("Version:", version.version);
  // ...
}

main();