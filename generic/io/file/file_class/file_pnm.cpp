#pragma once

file_pnm& file_pnm::open ( const path& pth )
{
    // Open file.
    file_interface::open(pth);

    // Read data.
    detail::read_from_boost_gil(self, path(self), boost::gil::pnm_tag(), depth());

    return self;
}

file_pnm& file_pnm::save ( )
{
    // Save file.
    file_interface::save();

    // Write data.
    detail::write_to_boost_gil(self, path(self), boost::gil::pnm_tag(), depth());

    return self;
}

int& file_pnm::depth ( )
{
    return image_depth;
}

const int& file_pnm::depth ( ) const
{
    return image_depth;
}
